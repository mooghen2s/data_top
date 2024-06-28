import os
import subprocess
import argparse
import requests
def main() -> None:
  if os.path.exists('tmp'):
    os.makedirs('tmp')
  dialog_file = f'output_{number_file}.txt'
  output_dat = f'output_{number_file}.dat'
  audio = f'output_{number_file}.mp3'
  audio_ogg = f'output_{number_file}.ogg'
  donwload_dialog_file = f"https://raw.githubusercontent.com/mooghen2s/data/top_tier_edge/top_tier_edge/output_{number_file}.txt"
  download_audio = f"https://raw.githubusercontent.com/mooghen2s/data/top_tier_edge/top_tier_edge/output_{number_file}.mp3"
  response = requests. get(donwload_dialog_file)
  if response.status_code == 200:
    with open(dialog_file, "wb") as file:
      file. write(response.content)
  response = requests. get(donwload_audio)
  if response.status_code == 200:
    with open(audio, "wb") as file:
      file. write(response.content)
  command = [
      'ffmpeg', '-y',
      '-loglevel', 'error',
      '-i', audio,
      '-ar', '16000', 
      audio
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
  os.unlink(audio_ogg)

  
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Nonton YouTube dengan profil tertentu.')
  parser.add_argument('profile_number', help='Nomor profil yang akan digunakan')
  args = parser.parse_args()
  number_file = args.profile_number
  main()
