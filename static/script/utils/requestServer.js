export async function requestServer(path, formatHtml=false, options = {}) {
  const tokenLocal = localStorage.getItem('token');
  const requestInfo = {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${tokenLocal}`,
      }
    }

    const response = await fetch(path, requestInfo);

    if(formatHtml){
        return response.text();
    } else {
        return response.json();
    }
}