const features = [
  ["Repository Intelligence", "Connect GitHub repositories or upload a project for indexed analysis."],
  ["Code Explanation", "Understand files, functions, dependencies, and design decisions with context."],
  ["AI Code Review", "Combine deterministic static analysis with contextual AI explanations."],
  ["Test Engineering", "Generate unit-test ideas, edge cases, mocks, and coverage targets."],
  ["Documentation Search", "Search project documentation and source chunks before asking AI."],
  ["Developer Chat", "Ask repository-aware questions while retaining conversation context."],
];

export default function Home() {
  return (
    <main style={{maxWidth: 1100, margin: "0 auto", padding: "64px 24px", fontFamily: "system-ui"}}>
      <p>CODEPILOT WORKSPACE</p>
      <h1>AI-powered engineering intelligence for your codebase.</h1>
      <p style={{maxWidth: 760}}>Understand unfamiliar repositories, review changes, design tests, search documentation, and collaborate with an AI assistant from one developer workspace.</p>
      <section style={{display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(280px,1fr))", gap: 18, marginTop: 40}}>
        {features.map(([title, description]) => <article key={title} style={{border: "1px solid #ddd", borderRadius: 12, padding: 22}}><h2>{title}</h2><p>{description}</p></article>)}
      </section>
    </main>
  );
}
