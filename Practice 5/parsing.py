import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()


datetime_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
    text
)
date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

payment_match = re.search(
    r"(Банковская карта|Наличные):\s*([\d\s]+,\d{2})",
    text
)
payment_method = payment_match.group(1) if payment_match else None
payment_amount = payment_match.group(2).replace(" ", "") if payment_match else None

total_match = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", text)
total = total_match.group(1).replace(" ", "") if total_match else None

product_pattern = re.findall(
    r"\d+\.\s*\n(.+?)\n(\d+,\d{3})\s*x\s*([\d\s]+,\d{2})\n([\d\s]+,\d{2})",
    text
)

products = []
all_prices = []
calculated_total = 0.0

for name, quantity, unit_price, item_total in product_pattern:
    quantity_clean = float(quantity.replace(",", "."))
    unit_price_clean = float(unit_price.replace(" ", "").replace(",", "."))
    item_total_clean = float(item_total.replace(" ", "").replace(",", "."))

    products.append({
        "name": name.strip(),
        "quantity": quantity_clean,
        "unit_price": unit_price_clean,
        "total_price": item_total_clean
    })

    all_prices.append(item_total.replace(" ", ""))
    calculated_total += item_total_clean

receipt_data = {
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "payment_amount": payment_amount,
    "total_from_receipt": total,
    "calculated_total": round(calculated_total, 2),
    "products": products,
    "all_prices": all_prices
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))

