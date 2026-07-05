import sys
import os
import json
import yaml
import xml.etree.ElementTree as ET

def xml_to_dict(elem):
    children = list(elem)
    if not children:
        return elem.text
    result = {}
    for child in children:
        result[child.tag] = xml_to_dict(child)
    return result

def load_xml(path):
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        print(f"Błąd składni XML: {e}")
        sys.exit(1)
    return xml_to_dict(tree.getroot())

def load_yaml(path):
    with open(path, encoding='utf-8') as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Błąd składni YAML: {e}")
            sys.exit(1)

def save_yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, allow_unicode=True)

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