const API_URL = 'http://localhost:5000';

export async function requestServer(path, formatHtml=false, options = {}) {
  const tokenLocal = localStorage.getItem('token');
  const requestInfo = {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${tokenLocal}`,
      }
    }

    const response = await fetch(API_URL + path, requestInfo);

    if(formatHtml){
        return response.text();
    } else {
        return response.json();
    }
}