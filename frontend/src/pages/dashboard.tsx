// src/pages/Dashboard.tsx
export default function Dashboard() {
  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-green-400">Dashboard</h2>
      
      {/* Status Overview */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-gray-800 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-gray-300 mb-2">Status</h3>
          <p className="text-2xl font-bold text-green-400">Ready</p>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-gray-300 mb-2">Bed Temp</h3>
          <p className="text-2xl font-bold text-orange-400">60°C</p>
          <p className="text-sm text-gray-400">Target: 60°C</p>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-gray-300 mb-2">Nozzle Temp</h3>
          <p className="text-2xl font-bold text-red-400">200°C</p>
          <p className="text-sm text-gray-400">Target: 200°C</p>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-lg">
          <h3 className="text-lg font-semibold text-gray-300 mb-2">Progress</h3>
          <p className="text-2xl font-bold text-blue-400">0%</p>
          <p className="text-sm text-gray-400">No active print</p>
        </div>
      </div>

      {/* Current Print */}
      <div className="bg-gray-800 p-6 rounded-lg">
        <h3 className="text-xl font-semibold text-green-400 mb-4">Current Print</h3>
        <div className="text-gray-300">
          <p className="mb-2">No print job active</p>
          <div className="bg-gray-700 rounded-full h-2 mb-2">
            <div className="bg-green-400 h-2 rounded-full" style={{ width: '0%' }}></div>
          </div>
          <div className="flex justify-between text-sm text-gray-400">
            <span>Time elapsed: --:--</span>
            <span>Time remaining: --:--</span>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="bg-gray-800 p-6 rounded-lg">
        <h3 className="text-xl font-semibold text-green-400 mb-4">Quick Actions</h3>
        <div className="flex gap-4">
          <button className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded transition-colors">
            Home All
          </button>
          <button className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded transition-colors">
            Preheat PLA
          </button>
          <button className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded transition-colors">
            Emergency Stop
          </button>
        </div>
      </div>
    </div>
  );
}