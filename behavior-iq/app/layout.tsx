import { Analytics } from '@vercel/analytics/next'
import type { Metadata, Viewport } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'BehaviorIQ — Sales Behavior Intelligence',
  description: 'Turn sales activity into measurable behavior, coaching, and revenue outcomes.',
  generator: 'BehaviorIQ',
}

export const viewport: Viewport = {
  colorScheme: 'light',
  themeColor: '#0f172a',
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en" className="bg-background"><body className="antialiased">{children}{process.env.NODE_ENV === 'production' && <Analytics />}</body></html>
}
