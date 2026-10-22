import { useEffect, useState } from 'react'

type Catalog = { id: string; title: string; controls: number }
type Hit = { id: string; title: string }

export default function App() {
  const [catalogs, setCatalogs] = useState<Catalog[]>([])
  const [catalog, setCatalog] = useState('')
  const [q, setQ] = useState('')
  const [hits, setHits] = useState<Hit[]>([])

  useEffect(() => {
    fetch('/api/catalogs')
      .then((r) => r.json())
      .then((c: Catalog[]) => {
        setCatalogs(c)
        if (c[0]) setCatalog(c[0].id)
      })
  }, [])

  useEffect(() => {
    if (!catalog) return
    fetch(`/api/catalogs/${catalog}/controls?q=${encodeURIComponent(q)}`)
      .then((r) => r.json())
      .then(setHits)
  }, [catalog, q])

  return (
    <main style={{ maxWidth: 800, margin: '2rem auto', fontFamily: 'system-ui' }}>
      <h1>neo-oscal</h1>
      <select value={catalog} onChange={(e) => setCatalog(e.target.value)}>
        {catalogs.map((c) => (
          <option key={c.id} value={c.id}>
            {c.title} ({c.controls})
          </option>
        ))}
      </select>{' '}
      <input placeholder="Control suchen…" value={q} onChange={(e) => setQ(e.target.value)} />
      <ul>
        {hits.map((h) => (
          <li key={h.id}>
            <code>{h.id}</code> {h.title}
          </li>
        ))}
      </ul>
    </main>
  )
}
