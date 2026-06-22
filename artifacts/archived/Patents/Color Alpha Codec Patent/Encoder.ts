import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import crc32 from "crc-32";

const colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Gray", "Black"];
const colorClasses: { [key: string]: string } = {
  Red: "bg-red-500",
  Orange: "bg-orange-500",
  Yellow: "bg-yellow-300",
  Green: "bg-green-500",
  Blue: "bg-blue-500",
  Purple: "bg-purple-500",
  Pink: "bg-pink-400",
  Gray: "bg-gray-500",
  Black: "bg-black text-white"
};
const symbols = ["A", "E", "F", "G", "H", "J", "K", "P", "R", "S", "T", "U", "V", "W", "X", "Y"];
const phonetics: { [key: string]: string } = {
  A: "Alpha", E: "Echo", F: "Foxtrot", G: "Golf", H: "Hotel",
  J: "Juliett", K: "Kilo", P: "Papa", R: "Romeo", S: "Sierra",
  T: "Tango", U: "Uniform", V: "Victor", W: "Whiskey", X: "X-ray", Y: "Yankee"
};

function getColorSymbol(index: number) {
  const color = colors[Math.floor(index / symbols.length) % colors.length];
  const symbol = symbols[index % symbols.length];
  return { color, symbol };
}

function calculateGroupCRC(indices: number[]): string {
  const binary = indices.map(i => i.toString(2).padStart(8, '0')).join('');
  return crc32.str(binary).toString(16).toUpperCase().slice(0, 2);
}

export default function TOTPSeedEncoder() {
  const [seedHex, setSeedHex] = useState("");
  const [output, setOutput] = useState<{ color: string; symbol: string }[][]>([]);

  const handleChange = (value: string) => {
    setSeedHex(value);
    const clean = value.replace(/[^0-9a-fA-F]/g, '').slice(0, 12); // 6 bytes max = 3 groups * 3 data pairs
    if (clean.length < 12) {
      setOutput([]);
      return;
    }
    const bytes = clean.match(/.{2}/g)!.map(hex => parseInt(hex, 16));
    const groups: { color: string; symbol: string }[][] = [];

    for (let g = 0; g < 3; g++) {
      const base = g * 3;
      const groupData = bytes.slice(base, base + 3);
      const crc = calculateGroupCRC(groupData);
      const indices = [...groupData, parseInt(crc, 16)];
      const group = indices.map(i => getColorSymbol(i));
      groups.push(group);
    }
    setOutput(groups);
  };

  return (
    <div className="p-6 space-y-4 max-w-xl mx-auto">
      <h2 className="text-xl font-bold text-center">TOTP Seed Encoder</h2>
      <Input
        type="text"
        placeholder="Enter up to 12 hex characters (6 bytes)"
        value={seedHex}
        onChange={(e) => handleChange(e.target.value)}
      />
      {output.length > 0 && output.map((group, gIndex) => (
        <div key={gIndex} className="grid grid-cols-4 gap-4">
          {group.map((entry, i) => (
            <Card key={i}>
              <CardContent className={`flex flex-col items-center justify-center p-4 rounded ${colorClasses[entry.color] || ''}`}>
                <div className="text-sm font-medium">{entry.color}</div>
                <div className="text-4xl font-bold">{entry.symbol}</div>
                <div className="text-sm text-white/80">{phonetics[entry.symbol] || ""}</div>
              </CardContent>
            </Card>
          ))}
        </div>
      ))}
    </div>
  );
}
