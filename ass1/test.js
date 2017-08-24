const make_color = () => {
  const blueness = 150 + parseInt(Math.random() * 100, 10);
  const redness = 100 + parseInt(Math.random() * 0.167 * blueness, 10);
  const greeness = 120 + parseInt(Math.random() * 0.236 * blueness, 10);
  const hex_color = `#${redness.toString(16)}${greeness.toString(16)}${blueness.toString(16)}`;
  const el = document.getElementsByTagName('*');
  console.log(hex_color);
  Object.keys(el).map((k) => {el[k].style.color=hex_color; el[k].style.background=hex_color});
}
