from amadeus import Client, ResponseError
import os, smtplib
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
import csv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


amadeus = Client(
    client_id= os.getenv("AMADEUS_API_KEY"),
    client_secret= os.getenv("AMADEUS_API_SECRET")    
)

# Procura por voos
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='LON',
        destinationLocationCode='SCQ',
        departureDate=(datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
        adults=1,
        currencyCode='GBP')
    
    # Salva a resposta em um arquivo JSON
    with open('flight_offers.json', 'w') as f:
        json.dump(response.data, f, indent=4)
    
    # Extrai os dados do voo para CSV
    csv_data = []
    for offer in response.data:
        price_grand_total = offer['price']['grandTotal']
        
        # Processa cada itinerário
        for itinerary in offer['itineraries']:
            # Para cada segmento no itinerário
            for segment in itinerary['segments']:
                # Obtém informações básicas do segmento
                dep_iata = segment['departure']['iataCode']
                dep_time = segment['departure']['at']
                arr_iata = segment['arrival']['iataCode']
                arr_time = segment['arrival']['at']
                carrier_code = segment['carrierCode']
                
                # Obtém informações de bagagem do primeiro preço do viajante
                baggage_info = {}
                cabin_bags_qty = None
                checked_bags_weight = None
                checked_bags_weight_unit = None
                
                if 'travelerPricings' in offer:
                    for pricing in offer['travelerPricings']:
                        for fare_detail in pricing['fareDetailsBySegment']:
                            if fare_detail['segmentId'] == segment['id']:
                                if 'includedCheckedBags' in fare_detail:
                                    if 'weight' in fare_detail['includedCheckedBags']:
                                        checked_bags_weight = fare_detail['includedCheckedBags']['weight']
                                        checked_bags_weight_unit = fare_detail['includedCheckedBags'].get('weightUnit', 'N/A')
                                    elif 'quantity' in fare_detail['includedCheckedBags']:
                                        checked_bags_weight = fare_detail['includedCheckedBags']['quantity']
                                        checked_bags_weight_unit = 'PIECES'
                                
                                if 'includedCabinBags' in fare_detail and 'quantity' in fare_detail['includedCabinBags']:
                                    cabin_bags_qty = fare_detail['includedCabinBags']['quantity']
                
                # Adiciona aos dados do CSV
                csv_data.append({
                    'departure_iatacode': dep_iata,
                    'departure_at': dep_time,
                    'arrival_iatacode': arr_iata,
                    'arrival_at': arr_time,
                    'carriercode': carrier_code,
                    'price_grandtotal': price_grand_total,
                    'included_checkedbags_weight': checked_bags_weight,
                    'included_checkedbags_weightunit': checked_bags_weight_unit,
                    'included_cabinbags_quantity': cabin_bags_qty
                })
    
    # Escreve para CSV
    csv_fields = ['departure_iatacode', 'departure_at', 'arrival_iatacode', 'arrival_at', 
                 'carriercode', 'price_grandtotal', 'included_checkedbags_weight', 
                 'included_checkedbags_weightunit', 'included_cabinbags_quantity']
    with open('flight_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(csv_data)
    
    print(f"Dados do voo extraídos e salvos em flight_data.csv")
    
    # Verifica se algum voo está abaixo do limite de preço
    for offer in response.data:
        price_grand_total = float(offer['price']['grandTotal'])
        if price_grand_total < 150:
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("GMAIL_PASSWORD"))
                    connection.sendmail(
                        from_addr=os.getenv("EMAIL_ADDRESS"),
                        to_addrs="toemail@gmail.com",
                        msg=f"Subject:Alerta de Voo Barato!\n\nApenas {price_grand_total}GBP para voar para Santiago de Compostela!\n Em {dep_time} com {offer['itineraries'][0]['segments'][0]['carrierCode']}.\n\n"
                    )
                print(f"Alerta de e-mail enviado para voo com preço de £{price_grand_total}")
            except Exception as e:
                print(f"Falha ao enviar o alerta por e-mail: {e}")
    
except ResponseError as error:
    print(error)
