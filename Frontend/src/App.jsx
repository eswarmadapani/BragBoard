import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
      <div className="max-w-md mx-auto bg-white rounded-xl shadow-lg p-8">
        <div className="flex justify-center space-x-4 mb-8">
          <a href="https://vite.dev" target="_blank" className="hover:scale-110 transition-transform">
            <img src={viteLogo} className="w-16 h-16" alt="Vite logo" />
          </a>
          <a href="https://react.dev" target="_blank" className="hover:scale-110 transition-transform">
            <img src={reactLogo} className="w-16 h-16 animate-spin" alt="React logo" />
          </a>
        </div>
        
        <h1 className="text-4xl font-bold text-center text-gray-800 mb-8">
          Vite + React + Tailwind
        </h1>
        
        <div className="bg-gray-50 rounded-lg p-6 mb-6">
          <button 
            onClick={() => setCount((count) => count + 1)}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors duration-200 shadow-md hover:shadow-lg"
          >
            Count is {count}
          </button>
          <p className="text-gray-600 text-center mt-4">
            Edit <code className="bg-gray-200 px-2 py-1 rounded text-sm">src/App.jsx</code> and save to test HMR
          </p>
        </div>
        
        <p className="text-center text-gray-500">
          Click on the Vite and React logos to learn more
        </p>
        
        {/* Tailwind Test Section */}
        <div className="mt-8 p-4 bg-green-100 border-l-4 border-green-500 rounded">
          <h3 className="text-lg font-semibold text-green-800 mb-2">🎉 Tailwind CSS Test</h3>
          <p className="text-green-700">
            If you can see this styled section with green background, Tailwind CSS is working perfectly!
          </p>
        </div>
      </div>
    </div>
  )
}

export default App
