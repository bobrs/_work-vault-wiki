import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import crc32 from "crc-32";

const colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Gray", "Black"];
const symbols = ["A", "E", "F", "G", "H", "J", "K", "P", "R", "S", "T", "U", "V", "W", "X", "Y"];
const phonetics = {
  A: "Alpha", E: "Echo", F: "Foxtrot", G: "Golf", H: "Hotel",
  J: "Juliett", K: "Kilo", P: "Papa", R: "Romeo", S: "Sierra",
  T: "Tango", U: "Uniform", V: "Victor", W: "Whiskey", X: "X-ray", Y: "Yankee"
};
const colorClasses = {
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

function getColorSymbol(index) {
  const color = colors[Math.floor(index / symbols.length) % colors.length];
  const symbol = symbols[index % symbols.length];
  return { color, symbol };
}

function getIndex(color, symbol) {
  const colorIndex = colors.indexOf(color);
  const symbolIndex = symbols.indexOf(symbol);
  if (colorIndex === -1 || symbolIndex === -1) return -1;
  return colorIndex * symbols.length + symbolIndex;
}

function toBinaryString(indices) {
  return indices.map(index => index.toString(2).padStart(8, '0')).join('');
}

function calculateGroupCRC(indices) {
  const bin = toBinaryString(indices);
  return crc32.str(bin).toString(16).toUpperCase().slice(0, 2);
}

export default function TotpSeedDemoApp() {
  const [seedHex, setSeedHex] = useState("");
  const [output, setOutput] = useState([]);
  const [selections, setSelections] = useState(Array(12).fill(0).map(() => ({ color: "", symbol: "" })));

  const updateSelection = (index, type, value) => {
    const updated = [...selections];
    updated[index] = { ...updated[index], [type]: value };
    setSelections(updated);
  };

  const handleChange = (value) => {
    setSeedHex(value);
    const clean = value.replace(/[^0-9a-fA-F]/g, '').slice(0, 12);
    if (clean.length < 12) {
      setOutput([]);
      return;
    }
    const bytes = clean.match(/.{2}/g).map(hex => parseInt(hex, 16));
    const groups = [];
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

  const indices = selections.map(({ color, symbol }) => getIndex(color, symbol));
  const validateGroup = (group) => {
    const base = group * 4;
    if (!indices.slice(base, base + 4).every(i => i >= 0)) return false;
    const data = indices.slice(base, base + 3);
    const crcActual = calculateGroupCRC(data);
    const crcEncoded = indices[base + 3].toString(16).toUpperCase().slice(-2);
    return crcActual === crcEncoded;
  };

  return (
    <div className="p-6 space-y-10 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold text-center">TOTP Seed Encoder & Decoder Demo</h1>

      <div>
        <h2 className="text-xl font-semibold mb-2">Encoder</h2>
        <Input
          type="text"
          placeholder="Enter up to 12 hex characters (6 bytes)"
          value={seedHex}
          onChange={(e) => handleChange(e.target.value)}
        />
        {output.length > 0 && output.map((group, gIndex) => (
          <div key={gIndex} className="grid grid-cols-4 gap-4 mt-4">
            {group.map((entry, i) => (
              <Card key={i}>
                <CardContent className={`flex flex-col items-center justify-center p-4 rounded ${colorClasses[entry.color]}`}>
                  <div className="text-sm font-medium">{entry.color}</div>
                  <div className="text-4xl font-bold">{entry.symbol}</div>
                  <div className="text-sm opacity-80">{phonetics[entry.symbol] || ""}</div>
                </CardContent>
              </Card>
            ))}
          </div>
        ))}
      </div>

      <div>
        <h2 className="text-xl font-semibold mb-2">Decoder</h2>
        {[0, 1, 2].map(groupIndex => {
          const base = groupIndex * 4;
          const isGroupFilled = selections.slice(base, base + 4).every(s => s.color && s.symbol);
          const isGroupValid = validateGroup(groupIndex);
          const borderClass = isGroupFilled ? (isGroupValid ? "border-green-500" : "border-red-500") : "border-gray-300";

          return (
            <div key={groupIndex} className={`grid grid-cols-2 gap-4 border-2 p-4 rounded mt-4 ${borderClass}`}>
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

        <div className="grid grid-cols-4 gap-4 mt-6">
          {selections.map((sel, i) => (
            <div key={i} className="flex flex-col gap-2">
              <Label>Color {i + 1}</Label>
              <Select onValueChange={val => updateSelection(i, "color", val)}>
                <SelectTrigger>
                  <SelectValue placeholder="Select color" />
                </SelectTrigger>
                <SelectContent>
                  {colors.map(color => (
                    <SelectItem key={color} value={color}>
                      <div className="flex items-center gap-2">
                        <span className={`w-4 h-4 rounded ${colorClasses[color].split(' ')[0]}`} title={color} />
                        {color}
                      </div>
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>

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
          ))}
        </div>
      </div>
    </div>
  );
}
