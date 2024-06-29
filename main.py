import edge_tts
import os
import shutil
import argparse
def main() -> None:
  dialog_file = f'output_{number_file}.txt'
  OUTPUT_FILE = f'output_{number_file}.mp3'
  with open(dialog_file, 'r', encoding='utf-8') as re_file:
    TEXT = re_file.readlines()
  VOICE = "zh-CN-YunxiaNeural"
  communicate = edge_tts.Communicate(str(TEXT), VOICE, rate="-10%")
  with open(OUTPUT_FILE, "wb") as file:
    for chunk in communicate.stream_sync():
      if chunk["type"] == "audio":
        file.write(chunk["data"])
      elif chunk["type"] == "WordBoundary":
        continue

  
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Nonton YouTube dengan profil tertentu.')
  parser.add_argument('profile_number', help='Nomor profil yang akan digunakan')
  args = parser.parse_args()
  number_file = args.profile_number
  main()
