import { useState, useEffect } from 'react'

import axios from 'axios'
import api from '../../shared/api'

function TestAuth() {
  async function getData() {
    console.log(await api.get('/api/test_2/'))
  }

  useEffect(() => {
    api.get('/api/test_2/')
  }, [])

  return (
    <>
      <div></div>
    </>
  )
}
export default TestAuth
