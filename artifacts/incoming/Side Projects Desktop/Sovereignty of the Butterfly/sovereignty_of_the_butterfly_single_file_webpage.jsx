import React, { useMemo, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Copy, Moon, Sun, Github, Download, Sparkles, Wind } from "lucide-react";

export default function ButterflySovereigntyPage() {
  const [dark, setDark] = useState(true);
  const [activeTab, setActiveTab] = useState("story");

  const tabs = [
    { id: "story", title: "Story", icon: Sparkles },
    { id: "axiom", title: "Axiom", icon: Wind },
    { id: "practice", title: "Practice", icon: Copy },
  ];

  const copyText = useMemo(() => ({
    story: `Once, in the kingdom of the Wind, there was a butterfly. She flapped her wings and made a breeze. Sometimes that breeze became a storm, though she never knew how.\n\nThe butterfly grew afraid, because she heard the storm’s thunder say: “You made me.” And fear whispered: “If I cause storms, I should never flap again.”\n\nBut in that land there was a law, written in neither book nor sky, called the Axiom of the Butterfly Nation: An agent retains sovereignty only if its act remains independent of feedback. If the wing waits for permission, it ceases to be a wing. If the choice bends to the echo, it ceases to be a choice.\n\nThe old moth explained: “Noise is everywhere. It fills the valleys like mist. Sometimes noise joins with your wingbeat and makes thunder. Sometimes it dies without trace. But sovereignty is not in the thunder. It is in the flap.”\n\nSo the butterfly practiced. She flapped as though no ear were listening. She flapped as though no storm could answer. The world shook sometimes—stochastic resonance can raise even whispers when the noise is tuned. Yet her sovereignty held, because she no longer asked, “What storm will this cause?” She asked only, “Am I the wing that flaps?”\n\nAnd the kingdom of the Wind survived, because the butterfly did not surrender her wings to the echo.`,
    axiom: `## Axiom of Butterfly Sovereignty\n\n**Definition.** An agent retains sovereignty only if its action remains locally determined and unconditioned by knowledge of systemic amplification. *Feedback-aware paralysis destroys freedom; feedback-blind action preserves it.*\n\n### Distinctions\n- **Butterfly Effect** — sensitive dependence: any flap might cascade.\n- **Stochastic Resonance** — noise + weak signal cross thresholds.\n- **Sovereignty Principle** — act without consulting the macro-feedback loop; otherwise choice collapses into simulation.\n\n### Implications\n- Design buffers that soften immediate feedback enslaving actors.\n- Act from integrity, not fear of optics.\n- Acknowledge consequences, but don’t let their echo cancel the possibility of action.\n\n> **Ethics note:** This is independence, not indifference. Consequences are real and borne after; they are not masters consulted before sovereignty exists.`,
    practice: `## Practice (Body)\n\n1. **Breath of the Wing** — 3 minutes. Inhale: “Wings belong to me.” Exhale: “Storms belong to the world.” Repeat.\n2. **One‑True‑Flap** — Choose a small act you’ve delayed from fear of reaction. Do it gently, as if unseen. Observe aftermath without self‑judgment.\n3. **Design Buffer** — In any system you build, insert a delay/threshold so people act before algorithms echo back at them. Prevent feedback‑prison.\n\n---\n\n**Mantra:**  
*Flap anyway. Wings are mine; echoes are not my master.*`,
  }), []);

  const gradient = dark
    ? "from-fuchsia-500/50 via-sky-500/40 to-emerald-500/50"
    : "from-fuchsia-400/40 via-sky-400/30 to-emerald-400/40";

  const onCopy = async () => {
    try {
      await navigator.clipboard.writeText(copyText[activeTab]);
      alert("Copied to clipboard ✨");
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className={`${dark ? "dark" : ""} h-full w-full`}> 
      <div className="min-h-screen bg-gradient-to-br from-zinc-50 via-zinc-100 to-zinc-200 dark:from-zinc-950 dark:via-zinc-900 dark:to-black text-zinc-800 dark:text-zinc-100 selection:bg-fuchsia-300/30 selection:text-fuchsia-900">
        <BackgroundButterflies />

        <header className="relative z-20 mx-auto flex w-full max-w-6xl items-center justify-between px-6 py-6">
          <div className="flex items-center gap-3">
            <ButterflyMark className="h-7 w-7" />
            <span className="text-lg font-semibold tracking-wide">Sovereignty of the Butterfly</span>
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
              className="rounded-2xl border border-zinc-700/50 bg-zinc-100/70 dark:bg-zinc-800/50 px-3 py-2 text-zinc-700 dark:text-zinc-200 backdrop-blur transition hover:scale-[1.02] hover:bg-zinc-200 dark:hover:bg-zinc-800 hidden sm:inline-flex"
            >
              <Github className="mr-2 h-4 w-4" /> Source
            </a>
          </div>
        </header>

        <section className="relative z-20 mx-auto max-w-3xl px-6 pb-20 pt-10">
          <div className="overflow-hidden rounded-3xl border border-zinc-200/50 dark:border-white/10 bg-white/80 dark:bg-white/5 p-0 shadow-2xl backdrop-blur-xl">
            <div className={`relative rounded-3xl bg-gradient-to-br ${gradient} p-8 sm:p-12`}> 
              <motion.h1
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
                className="text-balance text-3xl font-extrabold leading-tight text-zinc-900 dark:text-white drop-shadow sm:text-5xl"
              >
                Sovereignty of the Butterfly
              </motion.h1>
              <motion.p
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, delay: 0.15 }}
                className="mt-4 max-w-2xl text-zinc-700 dark:text-zinc-50/90 sm:text-lg"
              >
                A braided page of myth, axiom, and practice—designed to feel like a wingbeat.
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

            <div className="p-6 sm:p-10">
              <AnimatePresence mode="wait">
                <motion.article
                  key={activeTab}
                  initial={{ opacity: 0, y: 8 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -8 }}
                  transition={{ duration: 0.35 }}
                  className="prose dark:prose-invert max-w-none prose-p:leading-relaxed prose-h2:mt-6 prose-h2:mb-3 prose-h3:mt-5 prose-h3:mb-2 prose-strong:text-fuchsia-600 dark:prose-strong:text-fuchsia-400 prose-blockquote:border-fuchsia-400/50"
                  dangerouslySetInnerHTML={{ __html: copyText[activeTab].replace(/\n/g, '<br/>') }}
                />
              </AnimatePresence>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

function ButterflyMark({ className = "" }) {
  return (
    <svg className={className} viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#f0abfc" />
          <stop offset="50%" stopColor="#60a5fa" />
          <stop offset="100%" stopColor="#34d399" />
        </linearGradient>
      </defs>
      <path d="M32 30c-7-10-16-15-22-12s-5 14 8 18c-13 4-14 12-9 16s14 1 23-11" stroke="url(#g1)" strokeWidth="3" strokeLinecap="round" />
      <path d="M32 30c7-10 16-15 22-12s5 14-8 18c13 4 14 12 9 16s-14 1-23-11" stroke="url(#g1)" strokeWidth="3" strokeLinecap="round" />
      <circle cx="32" cy="34" r="2.5" fill="#e879f9" />
    </svg>
  );
}

function BackgroundButterflies() {
  const butterflies = Array.from({ length: 10 }).map((_, i) => ({
    id: i,
    x: Math.random() * 100,
    y: Math.random() * 100,
    delay: Math.random() * 6,
    scale: 0.6 + Math.random() * 0.9,
  }));

  return (
    <div className="pointer-events-none fixed inset-0 z-10 overflow-hidden">
      {butterflies.map((b) => (
        <motion.div
          key={b.id}
          initial={{ opacity: 0 }}
          animate={{ opacity: 0.25 }}
          transition={{ duration: 1.5, delay: b.delay }}
          className="absolute"
          style={{ left: `${b.x}%`, top: `${b.y}%` }}
        >
          <motion.div
            animate={{ y: [0, -12, 0], rotate: [-2, 2, -2] }}
            transition={{ repeat: Infinity, duration: 6 + b.delay, ease: "easeInOut" }}
            className="opacity-70"
          >
            <ButterflyGlow scale={b.scale} />
          </motion.div>
        </motion.div>
      ))}
    </div>
  );
}

function ButterflyGlow({ scale = 1 }) {
  return (
    <svg width={120 * scale} height={120 * scale} viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="rg" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#ffffff" stopOpacity="0.7" />
          <stop offset="60%" stopColor="#e879f9" stopOpacity="0.35" />
          <stop offset="100%" stopColor="#22d3ee" stopOpacity="0.15" />
        </radialGradient>
      </defs>
      <g filter="url(#f)">
        <path d="M60 60 C 20 10, 5 20, 18 44 C 2 50, 8 78, 30 78 C 42 78, 54 68, 60 60" fill="url(#rg)" />
        <path d="M60 60 C 100 10, 115 20, 102 44 C 118 50, 112 78, 90 78 C 78 78, 66 68, 60 60" fill="url(#rg)" />
        <circle cx="60" cy="62" r="4" fill="#f472b6" />
      </g>
      <defs>
        <filter id="f">
          <feGaussianBlur stdDeviation="3" />
        </filter>
      </defs>
    </svg>
  );
}
