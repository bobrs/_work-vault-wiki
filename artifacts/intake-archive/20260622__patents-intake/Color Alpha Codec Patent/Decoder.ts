import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import crc32 from "crc-32";

const colors = ["Red", "Green", "Blue", "Yellow"];

const colorClasses: { [key: string]: string } = {
  Red: "bg-red-500",
  Green: "bg-green-500",
  Blue: "bg-blue-500",
  Yellow: "bg-yellow-400"
};

const symbols = [..."ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"];
const phonetics: { [key: string]: string } = {
  A: "Alpha", B: "Bravo", C: "Charlie", D: "Delta", E: "Echo", F: "Foxtrot",
  G: "Golf", H: "Hotel", I: "India", J: "Juliett", K: "Kilo", L: "Lima",
  M: "Mike", N: "November", O: "Oscar", P: "Papa", Q: "Quebec", R: "Romeo",
  S: "Sierra", T: "Tango", U: "Uniform", V: "Victor", W: "Whiskey", X: "X-ray",
  Y: "Yankee", Z: "Zulu",
  0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
};

function getIndex(color: string, symbol: string): number {
  const colorIndex = colors.indexOf(color);
  const symbolIndex = symbols.indexOf(symbol);
  if (colorIndex === -1 || symbolIndex === -1) return -1;
  return colorIndex * symbols.length + symbolIndex;
}

function toBinaryString(indices: number[]): string {
  return indices.map(index => index.toString(2).padStart(8, '0')).join('');
}

function binaryToHex(bin: string): string {
  return parseInt(bin, 2).toString(16).toUpperCase().padStart(20, '0');
}

function calculateGroupCRC(indices: number[]): string {
  const bin = toBinaryString(indices);
  return crc32.str(bin).toString(16).toUpperCase().slice(0, 2); // 8 bits
}

export default function TOTPSeedDecoder() {
  const [selections, setSelections] = useState(
    Array(12).fill(0).map(() => ({ color: "", symbol: "" }))
  );

  const updateSelection = (index: number, type: "color" | "symbol", value: string) => {
    const updated = [...selections];
    updated[index] = { ...updated[index], [type]: value };
    setSelections(updated);
  };

  const indices = selections.map(({ color, symbol }) => getIndex(color, symbol));
  const isValidIndex = (i: number) => indices[i] >= 0;

  const validateGroup = (group: number): boolean => {
    const base = group * 4;
    if (!indices.slice(base, base + 4).every(index => index >= 0)) return false;
    const data = indices.slice(base, base + 3);
    const crcActual = calculateGroupCRC(data);
    const crcEncoded = indices[base + 3].toString(16).toUpperCase().slice(-2);
    return crcActual === crcEncoded;
  };

  return (
    <div className="p-6 space-y-4 max-w-2xl mx-auto">
      <h2 className="text-xl font-bold text-center">TOTP Seed Decoder (3 Blocks of 4)</h2>
      {[0, 1, 2].map(groupIndex => {
        const base = groupIndex * 4;
        const isGroupFilled = selections.slice(base, base + 4).every(s => s.color && s.symbol);
        const isGroupValid = validateGroup(groupIndex);
        const borderClass = isGroupFilled ? (isGroupValid ? "border-green-500" : "border-red-500") : "border-gray-300";

        return (
          <div key={groupIndex} className={`grid grid-cols-2 gap-4 border-2 p-4 rounded ${borderClass}`}>
            {selections.slice(base, base + 4).map((sel, j) => {
              const i = base + j;
              const colorClass = colorClasses[sel.color] || "bg-gray-200";
              return (
                <Card key={i}>
                  <CardContent className="flex justify-between items-center p-4 gap-4">
                    <div>
                      <Label>Color {i + 1}</Label>
                      <Select onValueChange={val => updateSelection(i, "color", val)}>
                        <SelectTrigger>
                          <SelectValue placeholder="Select color" />
                        </SelectTrigger>
                        <SelectContent>
                          {colors.map(color => (
                            <SelectItem key={color} value={color}>
                              <div className="flex items-center gap-2">
                                <span className={`w-4 h-4 rounded ${colorClasses[color]}`} title={color} />
                                {color}
                              </div>
                            </SelectItem>
                          ))}
                        </SelectContent>
                      </Select>
                    </div>
                    <div className={`w-16 h-16 rounded flex items-center justify-center text-4xl font-bold text-white ${colorClass}`} title={`Color: ${sel.color}, Symbol: ${sel.symbol}`}>
                      {sel.symbol || ""}
                    </div>
                    <div>
                      <Label>Symbol {i + 1}</Label>
                      <Select onValueChange={val => updateSelection(i, "symbol", val)}>
                        <SelectTrigger>
                          <SelectValue placeholder="Select symbol" />
                        </SelectTrigger>
                        <SelectContent>
                          {symbols.map(symbol => (
                            <SelectItem key={symbol} value={symbol}>
                              <div className="flex items-center gap-2">
                                <span className="w-6 text-left font-mono">{symbol}</span>
                                <span className="text-sm text-gray-500">{phonetics[symbol]}</span>
                              </div>
                            </SelectItem>
                          ))}
                        </SelectContent>
                      </Select>
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        );
      })}
    </div>
  );
}
