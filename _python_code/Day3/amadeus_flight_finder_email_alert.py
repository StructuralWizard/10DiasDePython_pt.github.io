from amadeus import Client, ResponseError
import os, smtplib
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
import csv

# Load environment variables from .env file
load_dotenv()


amadeus = Client(
    client_id= os.getenv("AMADEUS_API_KEY"),
    client_secret= os.getenv("AMADEUS_API_SECRET")    
)

# Search for flights
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='LON',
        destinationLocationCode='SCQ',
        departureDate=(datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
        adults=1,
        currencyCode='GBP')
    
    # Save response to a JSON file
    with open('flight_offers.json', 'w') as f:
        json.dump(response.data, f, indent=4)
    
    # Extract flight data for CSV
    csv_data = []
    for offer in response.data:
        price_grand_total = offer['price']['grandTotal']
        
        # Process each itinerary
        for itinerary in offer['itineraries']:
            # For each segment in the itinerary
            for segment in itinerary['segments']:
                # Get basic segment info
                dep_iata = segment['departure']['iataCode']
                dep_time = segment['departure']['at']
                arr_iata = segment['arrival']['iataCode']
                arr_time = segment['arrival']['at']
                carrier_code = segment['carrierCode']
                
                # Get baggage info from the first traveler pricing
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
                
                # Add to CSV data
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
    
    # Write to CSV
    csv_fields = ['departure_iatacode', 'departure_at', 'arrival_iatacode', 'arrival_at', 
                 'carriercode', 'price_grandtotal', 'included_checkedbags_weight', 
                 'included_checkedbags_weightunit', 'included_cabinbags_quantity']
    with open('flight_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(csv_data)
    
    print(f"Flight data extracted and saved to flight_data.csv")
    
    # Check if any flights are below price threshold
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
                        msg=f"Subject:Cheap Flight Alert!\n\nOnly {price_grand_total}GBP to fly to Santiago de Compostela!\n On the {dep_time} with {offer['itineraries'][0]['segments'][0]['carrierCode']}.\n\n"
                    )
                print(f"Email alert sent for flight priced at £{price_grand_total}")
            except Exception as e:
                print(f"Failed to send email alert: {e}")
    
except ResponseError as error:
    print(error)