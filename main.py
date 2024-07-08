import edge_tts
import os
import subprocess
import argparse
import re
def main() -> None:
  if not os.path.exists('out'):
    os.makedirs('out')
  dialog_file = f'output_{number_file}.txt'
  dialog_files = f'out/output_{number_file}.txt'
  OUTPUT_FILE = f'out/output_{number_file}.mp3'
  VOICE = "zh-CN-YunxiaNeural"
  with open(dialog_file, 'r', encoding='utf-8') as res_file:
    with open(dialog_files, 'w', encoding='utf-8') as file:
      for linex in res_file:
        if re.search(r'[a-zA-Z0-9]', linex):
          file.write(linex)
  with open(dialog_files, 'r', encoding='utf-8') as re_file:
    with open(OUTPUT_FILE, "wb") as au_file:
      for line in re_file:
        if re.search(r'[a-zA-Z0-9]', line):
          try:
            communicate = edge_tts.Communicate(line, VOICE, rate="-10%")
            for chunk in communicate.stream_sync():
              if chunk["type"] == "audio":
                au_file.write(chunk["data"])
              elif chunk["type"] == "WordBoundary":
                continue
          except Exception as e:  print("Error tts:", str(e)) 
  dialog_file = f'out/output_{number_file}.txt'
  output_dat = f'out/output_{number_file}.dat'
  audio = f'out/output_{number_file}.mp3'
  audio_ogg = f'output_{number_file}.ogg'
  command = [
      'ffmpeg', '-y',
      '-loglevel', 'error',
      '-i', audio,
      '-ar', '16000', 
      audio_ogg
  ]
  subprocess.run(command)
  command = [
      './rhubarb',
      '-q',
      '-d', dialog_file,
      '-r', 'phonetic', 
      '--threads', '4',
      '-f', 'dat',
      '--datFrameRate', '15',
      '-o', output_dat,
      '--extendedShapes', 'xhg',
      audio_ogg
  ]
  subprocess.run(command)
  print(f'done for: {audio}')

  
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Nonton YouTube dengan profil tertentu.')
  parser.add_argument('profile_number', help='Nomor profil yang akan digunakan')
  args = parser.parse_args()
  number_file = args.profile_number
  main()
