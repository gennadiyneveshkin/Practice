def build_note (note_text:str, note_name:str):
    with open(f'{note_name}.txt', 'w', encoding="utf-8") as f:
        f.write(note_text)
