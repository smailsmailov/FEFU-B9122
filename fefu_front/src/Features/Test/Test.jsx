import { useState, useEffect } from 'react'

import axios from 'axios'
import api from '../../shared/api'

function Test() {
  const [loading, setLoading] = useState(true)
  const [data, setData] = useState('')
  const [error, setError] = useState(null)

  async function getData() {
    console.log(await api.post('/api/test_1/', { name: 'qweasdzcx' }))
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        api
          .get('/api/test/')
          .then(response => {
            console.log(response)
            setData(response)
          })
          .catch(error => console.error(error))

        getData()
      } catch (err) {
        setError(err)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error ^_^</div>

  return (
    <>
      <div>{data}</div>
    </>
  )
}
export default Test
