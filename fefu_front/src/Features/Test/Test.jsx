import { useState } from 'react'

 function Test({name}) {
  const [count, setCount] = useState(0)

  const handleBtn = () => {
    setCount(count + 1 )
  }

  const handleMinBtn = () => {
    setCount(count - 1 )
  }

  return (
    <>
      <div>
          <p>
            {count}
          </p>
            <button onClick={handleMinBtn}>-</button>
            <button onClick={handleBtn}>+</button>
      </div>
    </>
  )
}
export default Test
