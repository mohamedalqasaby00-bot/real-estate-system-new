const fs = require('fs');
const html = fs.readFileSync('./public/index.html', 'utf8');
const worker = 'const HTML = `' + html + '`;\n\nexport default {\n  async fetch(request) {\n    return new Response(HTML, {\n      headers: { \'content-type\': \'text/html;charset=UTF-8\' }\n    });\n  }\n};\n';
fs.writeFileSync('./worker.js', worker, 'utf8');
console.log('worker.js size:', fs.statSync('./worker.js').size, 'bytes');
