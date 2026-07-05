import sys
import os
import json

def load_json(path):
    with open(path, encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Błąd składni JSON: {e}")
            sys.exit(1)

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def parse_args():
    if len(sys.argv) != 3:
        print("Użycie: program.exe plikWejsciowy.x plikWyjsciowy.y")
        sys.exit(1)

    in_path, out_path = sys.argv[1], sys.argv[2]

    if not os.path.isfile(in_path):
        print(f"Błąd: plik wejściowy '{in_path}' nie istnieje.")
        sys.exit(1)

    in_ext = os.path.splitext(in_path)[1].lower()
    out_ext = os.path.splitext(out_path)[1].lower()

    supported = {'.json', '.xml', '.yml', '.yaml'}
    if in_ext not in supported:
        print(f"Błąd: nieobsługiwany format wejściowy '{in_ext}'.")
        sys.exit(1)
    if out_ext not in supported:
        print(f"Błąd: nieobsługiwany format wyjściowy '{out_ext}'.")
        sys.exit(1)

    return in_path, out_path, in_ext, out_ext

def main():
    in_path, out_path, in_ext, out_ext = parse_args()
    print(f"Wejście: {in_path} ({in_ext}) ---> Wyjście: {out_path} ({out_ext})")

if __name__ == '__main__':
    main()