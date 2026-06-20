from aiogram import types
from countries import COUNTRIES
from generator import generate_code, generate_number

def main_menu():
    return types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📞 الحصول على رقم", callback_data="get_number")]
    ])

def countries_menu():
    buttons = []
    row = []

    for key, data in COUNTRIES.items():
        row.append(
            types.InlineKeyboardButton(
                text=f"{data['flag']} {data['name']}",
                callback_data=f"country_{key}"
            )
        )

        if len(row) == 2:
            buttons.append(row)
            row = []

    if row:
        buttons.append(row)

    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def build_result(country):
    code = generate_code()
    number = generate_number(country["code"])

    text = f"""
𝐀𝐋𝐌𝐍𝐇𝐑𝐅 𓊈𝑽꯭𝑰𝑷𓊉

#𝐈𝐍 | {country['flag']} {country['name']}
📞 {number}

🔐 Code: {code}
"""

    return text, code
