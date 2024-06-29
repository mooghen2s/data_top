import os
import subprocess
import argparse
def main() -> None:
  dialog_file = f'output_{number_file}.txt'
  output_dat = f'output_{number_file}.dat'
  audio = f'output_{number_file}.mp3'
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
