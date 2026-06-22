import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import crc32 from "crc-32";

const colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Gray", "Black"];
const colorClasses: { [key: string]: string } = {
  Red: "bg-red-500 text-white",
  Orange: "bg-orange-500 text-white",
  Yellow: "bg-yellow-300 text-black",
  Green: "bg-green-500 text-white",
  Blue: "bg-blue-500 text-white",
  Purple: "bg-purple-500 text-white",
  Pink: "bg-pink-400 text-black",
  Gray: "bg-gray-500 text-white",
  Black: "bg-black text-white"
};
const symbols = ["A", "E", "F", "G", "H", "J", "K", "P", "R", "S", "T", "U", "V", "W", "X", "Y"];
const phonetics: { [key: string]: string } = {
  A: "Alpha", E: "Echo", F: "Foxtrot", G: "Golf", H: "Hotel",
  J: "Juliett", K: "Kilo", P: "Papa", R: "Romeo", S: "Sierra",
  T: "Tango", U: "Uniform", V: "Victor", W: "Whiskey", X: "X-ray", Y: "Yankee"
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

function calculateGroupCRC(indices: number[]): string {
  const bin = toBinaryString(indices);
  return crc32.str(bin).toString(16).toUpperCase().slice(0, 2);
}

export default function TOTPSeedDecoderFinal() {
  const [selections, setSelections] = useState(
    Array(12).fill(0).map(() => ({ color: "", symbol: "" }))
  );

  const updateSelection = (index: number, type: "color" | "symbol", value: string) => {
    const updated = [...selections];
    updated[index] = { ...updated[index], [type]: value };
    setSelections(updated);
  };

  const indices = selections.map(({ color, symbol }) => getIndex(color, symbol));

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
      <h2 className="text-xl font-bold text-center">TOTP Seed Decoder</h2>
      {[0, 1, 2].map(groupIndex => {
        const base = groupIndex * 4;
        const isGroupFilled = selections.slice(base, base + 4).every(s => s.color && s.symbol);
        const isGroupValid = validateGroup(groupIndex);
        const borderClass = isGroupFilled ? (isGroupValid ? "border-green-500" : "border-red-500") : "border-gray-300";

        return (
          <div key={groupIndex} className={`grid grid-cols-2 gap-4 border-2 p-4 rounded ${borderClass}`}>
            {selections.slice(base, base + 4).map((sel, j) => {
              const i = base + j;
              const colorClass = colorClasses[sel.color] || "bg-gray-200 text-black";
              return (
                <Card key={i}>
                  <CardContent className={`flex flex-col items-center justify-center p-4 rounded ${colorClass}`}>
                    <div className="text-sm font-medium">{sel.color}</div>
                    <div className="text-4xl font-bold">{sel.symbol}</div>
                    <div className="text-sm opacity-80">{phonetics[sel.symbol] || ""}</div>
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
