// Render arithmatex math (generic mode) with KaTeX; re-runs on Material's instant navigation.
document$.subscribe(() => {
  renderMathInElement(document.body, {
    delimiters: [
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false },
    ],
  });
});
