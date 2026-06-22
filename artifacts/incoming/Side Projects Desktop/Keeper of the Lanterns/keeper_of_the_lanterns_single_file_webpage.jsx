import React, { useMemo, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Lamp, Flame, Droplets, Compass, Shield, Copy, Moon, Sun, Github, Download, Sparkles } from "lucide-react";

// ------------------------------------------------------------
// KEEPER OF THE LANTERNS — Single‑file React page
// Tailwind + Framer Motion, same vibe as the Butterfly page
// ------------------------------------------------------------

export default function KeeperOfLanternsPage() {
  const [dark, setDark] = useState(true);
  const [activeTab, setActiveTab] = useState("story");

  const tabs = [
    { id: "story", title: "Story", icon: Lamp },
    { id: "rules", title: "Rules", icon: Flame },
    { id: "playbook", title: "Playbook", icon: Compass },
  ];

  const copyText = useMemo(() => ({
    story: `
      <p>Picture yourself as a keeper of lanterns. You've got a pouch of oil — your time, your money, your attention — and three lanterns flicker in front of you. Your goal: keep all of them glowing through the night.</p>
      <p><strong>First rule: floors first.</strong> If a lantern is about to sputter out, give it oil. No point polishing the glass on another lamp while one goes dark. This is the <em>basic needs</em> step: nutrition, safety, sleep, simple kindness.</p>
      <p><strong>Second rule: margins matter.</strong> Once every lantern is lit, ask: where does the next drop of oil make the biggest glow? Sometimes one lamp turns a tiny drop into a beam, while another barely changes. Put oil where the glow grows fastest.</p>
      <p><strong>Third rule: hedge against the wind.</strong> If a storm blows through, all the lamps flicker together. That's why you spread the oil around enough that none are fragile. And sometimes you discover one lamp is shielded while another is exposed; then you adjust, because fairness doesn’t mean sameness — it means none are left to fail.</p>
      <p><strong>Fourth rule: test and learn.</strong> Not every wick burns the same. Maybe one lantern burns brighter with less oil, maybe another gulps it hungrily. You don't know until you try. So you experiment, holding back a little oil to see what happens when you tilt the flask differently. That's the exploration fund — your 10% for surprises.</p>
      <p><strong>Fifth rule: relationships count.</strong> If one lantern feels ignored, it doesn't just dim, it whispers to the others: <em>“This keeper is unfair.”</em> And then trust erodes, and suddenly the light you thought you bought with oil burns half as bright. So fairness is not just decoration; it's fuel.</p>
      <p>At the end of the night, what matters is not that one lamp shone like a lighthouse while the others went dark. It's that <strong>all three were still burning when the dawn arrived.</strong> Because in the long run, survival and togetherness make more light than brilliance alone.</p>
    `,
    rules: `
      <h2>Five Rules for the Lantern Keeper</h2>
      <ol>
        <li><strong>Floors First.</strong> Fund basics before polish: food, sleep, safety, quiet attention. A lamp on the edge gets oil <em>now</em>.</li>
        <li><strong>Equalize Margins.</strong> After floors, place the next drop where it makes the <em>biggest additional glow</em>. Diminishing returns mean you’ll usually spread oil.</li>
        <li><strong>Hedge the Wind.</strong> When one gust can shake every lamp, avoid over‑concentrating. Give each enough resilience that no single storm ends the night.</li>
        <li><strong>Explore, then Focus.</strong> Keep a 10–20% reserve to try new wicks, shades, and placements. When something clearly works, lean in.</li>
        <li><strong>Protect the Fabric.</strong> Perceived unfairness is a leak in the oil can. Make care visible; rotate spotlights; talk about choices. Trust multiplies light.</li>
      </ol>
      <div class="mt-6 grid gap-3 sm:grid-cols-2">
        <div class="rounded-xl border border-white/10 bg-white/5 p-4"><h3 class="font-semibold">Shared Light</h3><p>Choose investments that lift many at once: family reading hour, a calm evening routine, a shared nature walk.</p></div>
        <div class="rounded-xl border border-white/10 bg-white/5 p-4"><h3 class="font-semibold">Idiosyncratic Shine</h3><p>Some lanterns respond uniquely — honor a child’s spark with a little extra, without starving the rest.</p></div>
      </div>
    `,
    playbook: `
      <h2>The 7‑Step Lantern Playbook</h2>
      <ol>
        <li><strong>List floors</strong> for each child (sleep, food, safety, school basics) — fund these first.</li>
        <li><strong>Name 3–5 bets</strong> for this week’s extra oil (time/money).</li>
        <li><strong>Score marginal gain</strong> for each bet (gut is fine): which adds the most <em>additional</em> glow?</li>
        <li><strong>Allocate the next drop</strong> to the top scorer; repeat until marginals feel even.</li>
        <li><strong>Diversify</strong> against shared shocks; prefer shared goods when they brighten everyone.</li>
        <li><strong>Reserve 10–20%</strong> for experiments and surprises.</li>
        <li><strong>Review on a cadence</strong> (weekly for time, monthly for money) and reshuffle by what you observed, not what you hoped.</li>
      </ol>
      <hr class="my-6 opacity-50"/>
      <p class="text-sm opacity-80"><strong>One‑minute example:</strong> You have 10 hours. Child A: reading jump (0.8/hr). Child B: piano (0.4). Child C: soccer (0.5). Family museum (0.9 total). Allocate ~3h A, 2h C, 2h B, 2h museum, 1h try coding club. Re‑measure next week.</p>
    `,
  }), []);

  const gradient = dark
    ? "from-rose-500/40 via-amber-400/30 to-cyan-500/40"
    : "from-rose-400/40 via-amber-300/30 to-cyan-400/40";

  const onCopy = async () => {
    try {
      await navigator.clipboard.writeText(copyText[activeTab].replace(/<[^>]+>/g, ''));
      alert("Copied to clipboard ✨");
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className={`${dark ? "dark" : ""} h-full w-full`}>
      <div className="min-h-screen bg-gradient-to-br from-zinc-50 via-zinc-100 to-zinc-200 dark:from-zinc-950 dark:via-zinc-900 dark:to-black text-zinc-800 dark:text-zinc-100 selection:bg-amber-300/30 selection:text-amber-900">
        <BackgroundLanterns />

        {/* Nav */}
        <header className="relative z-20 mx-auto flex w-full max-w-6xl items-center justify-between px-6 py-6">
          <div className="flex items-center gap-3">
            <LanternMark className="h-7 w-7" />
            <span className="text-lg font-semibold tracking-wide">Keeper of the Lanterns</span>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={() => setDark((d) => !d)}
              className="rounded-2xl border border-zinc-700/50 bg-zinc-100/70 dark:bg-zinc-800/50 px-3 py-2 text-zinc-700 dark:text-zinc-200 backdrop-blur transition hover:scale-[1.02] hover:bg-zinc-200 dark:hover:bg-zinc-800"
              aria-label="Toggle theme"
            >
              {dark ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
            </button>
            <a
              href="#source"
              className="hidden sm:inline-flex rounded-2xl border border-zinc-700/50 bg-zinc-100/70 dark:bg-zinc-800/50 px-3 py-2 text-zinc-700 dark:text-zinc-200 backdrop-blur transition hover:scale-[1.02] hover:bg-zinc-200 dark:hover:bg-zinc-800"
            >
              <Github className="mr-2 h-4 w-4" /> Source
            </a>
          </div>
        </header>

        {/* Hero */}
        <section className="relative z-20 mx-auto max-w-3xl px-6 pb-16 pt-8">
          <div className="overflow-hidden rounded-3xl border border-zinc-200/50 dark:border-white/10 bg-white/80 dark:bg-white/5 p-0 shadow-2xl backdrop-blur-xl">
            <div className={`relative rounded-3xl bg-gradient-to-br ${gradient} p-8 sm:p-12`}>
              <motion.h1
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
                className="text-balance text-3xl font-extrabold leading-tight text-zinc-900 dark:text-white drop-shadow sm:text-5xl"
              >
                Keeper of the Lanterns
              </motion.h1>
              <motion.p
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, delay: 0.15 }}
                className="mt-4 max-w-2xl text-zinc-700 dark:text-zinc-50/90 sm:text-lg"
              >
                A practical parable on allocating love, time, and means so <em>every light</em> makes it to dawn.
              </motion.p>

              <div className="mt-8 flex flex-wrap items-center gap-3">
                {tabs.map((t) => (
                  <button
                    key={t.id}
                    onClick={() => setActiveTab(t.id)}
                    className={`group flex items-center gap-2 rounded-full border px-4 py-2 text-sm transition ${
                      activeTab === t.id
                        ? "border-zinc-900 dark:border-white/80 bg-zinc-200 dark:bg-white/20 text-zinc-900 dark:text-white shadow"
                        : "border-zinc-400/30 dark:border-white/20 bg-zinc-100/50 dark:bg-white/10 text-zinc-700 dark:text-white/80 hover:border-zinc-600/50 dark:hover:border-white/40 hover:text-zinc-900 dark:hover:text-white"
                    }`}
                  >
                    <t.icon className="h-4 w-4" />
                    {t.title}
                  </button>
                ))}
                <button
                  onClick={onCopy}
                  className="ml-auto rounded-full border border-zinc-400/30 dark:border-white/30 bg-zinc-100/70 dark:bg-white/10 px-4 py-2 text-sm text-zinc-700 dark:text-white/90 transition hover:border-zinc-600/50 dark:hover:border-white/50 hover:text-zinc-900 dark:hover:text-white"
                >
                  <Copy className="mr-2 inline h-4 w-4" /> Copy section
                </button>
              </div>
            </div>

            {/* Body */}
            <div className="p-6 sm:p-10">
              <AnimatePresence mode="wait">
                <motion.article
                  key={activeTab}
                  initial={{ opacity: 0, y: 8 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -8 }}
                  transition={{ duration: 0.35 }}
                  className="prose dark:prose-invert max-w-none prose-p:leading-relaxed prose-h2:mt-6 prose-h2:mb-3 prose-h3:mt-5 prose-h3:mb-2 prose-strong:text-amber-700 dark:prose-strong:text-amber-300 prose-blockquote:border-amber-400/50"
                  dangerouslySetInnerHTML={{ __html: copyText[activeTab] }}
                />
              </AnimatePresence>

              {activeTab === "playbook" && (
                <div className="mt-6 grid gap-4 sm:grid-cols-2">
                  <DownloadCard title="Download all text" content={[copyText.story, copyText.rules, copyText.playbook].join('\n\n---\n\n').replace(/<[^>]+>/g, '')} />
                  <ShareCard />
                </div>
              )}
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="relative z-20 mx-auto max-w-3xl px-6 pb-12 text-sm text-zinc-500">
          <p>Built as a sister page to <em>Sovereignty of the Butterfly</em>. Colors whisper lantern‑light; shapes are generative.</p>
          <p id="source" className="mt-1 opacity-75">Text & design © You — remix, host, and share freely.</p>
        </footer>
      </div>
    </div>
  );
}

// ------------------------------------------------------------
// Decorative components (lantern marks + background glows)
// ------------------------------------------------------------
function LanternMark({ className = "" }) {
  return (
    <svg className={className} viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#fb7185" />
          <stop offset="50%" stopColor="#f59e0b" />
          <stop offset="100%" stopColor="#22d3ee" />
        </linearGradient>
      </defs>
      <path d="M20 22h24a2 2 0 012 2v12a2 2 0 01-2 2H20a2 2 0 01-2-2V24a2 2 0 012-2z" stroke="url(#lg)" strokeWidth="3" strokeLinecap="round" />
      <path d="M32 14v36" stroke="url(#lg)" strokeWidth="3" strokeLinecap="round" />
      <circle cx="32" cy="32" r="4" fill="#fbbf24" />
    </svg>
  );
}

function BackgroundLanterns() {
  const lights = Array.from({ length: 9 }).map((_, i) => ({
    id: i,
    x: Math.random() * 100,
    y: Math.random() * 100,
    delay: Math.random() * 6,
    scale: 0.6 + Math.random() * 1.1,
  }));

  return (
    <div className="pointer-events-none fixed inset-0 z-10 overflow-hidden">
      {lights.map((l) => (
        <motion.div
          key={l.id}
          initial={{ opacity: 0 }}
          animate={{ opacity: 0.22 }}
          transition={{ duration: 1.8, delay: l.delay }}
          className="absolute"
          style={{ left: `${l.x}%`, top: `${l.y}%` }}
        >
          <motion.div
            animate={{ y: [0, -10, 0], rotate: [-1, 1, -1] }}
            transition={{ repeat: Infinity, duration: 7 + l.delay, ease: "easeInOut" }}
          >
            <LanternGlow scale={l.scale} />
          </motion.div>
        </motion.div>
      ))}
    </div>
  );
}

function LanternGlow({ scale = 1 }) {
  return (
    <svg width={120 * scale} height={120 * scale} viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="rg2" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#ffffff" stopOpacity="0.7" />
          <stop offset="60%" stopColor="#f59e0b" stopOpacity="0.35" />
          <stop offset="100%" stopColor="#fb7185" stopOpacity="0.15" />
        </radialGradient>
      </defs>
      <g filter="url(#f2)">
        <rect x="30" y="30" width="60" height="40" rx="10" fill="url(#rg2)" />
        <circle cx="60" cy="50" r="5" fill="#fbbf24" />
      </g>
      <defs>
        <filter id="f2">
          <feGaussianBlur stdDeviation="3" />
        </filter>
      </defs>
    </svg>
  );
}

// ------------------------------------------------------------
// Utility cards
// ------------------------------------------------------------
function DownloadCard({ title, content }) {
  const handleDownload = () => {
    const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "keeper_of_the_lanterns.txt";
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur">
      <h4 className="mb-2 font-semibold text-white/90">{title}</h4>
      <button
        onClick={handleDownload}
        className="rounded-full border border-white/30 bg-white/10 px-4 py-2 text-sm text-white/90 transition hover:border-white/50 hover:text-white"
      >
        <Download className="mr-2 inline h-4 w-4" /> Download .txt
      </button>
    </div>
  );
}

function ShareCard() {
  const share = async () => {
    const text = `Keeper of the Lanterns — a parable for allocating love, time, and means.`;
    const url = window.location.href;
    if (navigator.share) {
      try { await navigator.share({ title: "Keeper of the Lanterns", text, url }); } catch {}
    } else {
      await navigator.clipboard.writeText(`${text}\n${url}`);
      alert("Share link copied ✨");
    }
  };
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur">
      <h4 className="mb-2 font-semibold text-white/90">Share</h4>
      <button
        onClick={share}
        className="rounded-full border border-white/30 bg-white/10 px-4 py-2 text-sm text-white/90 transition hover:border-white/50 hover:text-white"
      >
        Share link
      </button>
    </div>
  );
}
