import React from 'react'

export const Modal = ({ onModalClose, image, prediction, confidence} ) => {

  return (
    <div className="fixed top-0 left-0 w-full h-full bg-gray-900 bg-opacity-50 flex items-center justify-center">
      <div className="bg-white w-2/3 w-2/3 p-16 rounded-2xl flex flex-col items-center justify-center">
        <img className="w-2/3 object-contain rounded-2xl mb-6" src={image} alt="preview" />
        <p className="font-thin text-2xl"><span className="font-normal">prediction:</span> {prediction}</p>
        <p className="font-thin text-2xl mb-3"><span className="font-normal">confidence:</span> {(100 * confidence).toFixed(2)}%</p>
        <button className="bg-indigo-600 hover:bg-neutral-200 text-white font-bold py-1 px-4 border border-solid border-neutral-300 rounded" onClick={onModalClose}>Close</button>
      </div>
  </div>
  )
}
