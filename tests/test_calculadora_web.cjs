const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const html = fs.readFileSync(path.join(process.cwd(), 'index.html'), 'utf8');

test('El HTML muestra el titulo de la calculadora', () => {
  assert.match(html, /<h1[^>]*>\s*Mi calculadora\b/i);
});

test('El formulario contiene entradas y resultado', () => {
  for (const id of ['formulario', 'numero1', 'numero2', 'operacion', 'resultado']) {
    assert.match(html, new RegExp(`id=["']${id}["']`), `Falta el elemento ${id}`);
  }
});

test('El JavaScript incluye las cuatro operaciones', () => {
  for (const operacion of ['sumar', 'restar', 'multiplicar', 'dividir']) {
    assert.match(html, new RegExp(`case ['"]${operacion}['"]`), `Falta ${operacion}`);
  }
});

test('La pagina anuncia la fase corregida', () => {
  assert.match(html, /Fase 2:\s*prueba corregida/i);
});
