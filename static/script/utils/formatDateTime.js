export function getDateReserve(_datetime){
    _datetime = new Date(_datetime);

    return _datetime.toLocaleDateString('pt-BR', {
        timeZone: 'America/Sao_Paulo'
    });
}
export function getTimeReserve(_datetime){
    _datetime = new Date(_datetime);
    
    return _datetime.toLocaleTimeString('pt-BR', {
        timeZone: 'America/Sao_Paulo',
        hour: '2-digit',
        minute: '2-digit'
    });
}

export function validateDateTime(dateInput, timeStart, timeEnd){
  const start = new Date(`${dateInput}T${timeStart}`);
  let end = new Date(`${dateInput}T${timeEnd}`);

  if (start > end) {
    end.setDate(end.getDate() + 1);
  }

  const formatDateTime = (date) => {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");

    return `${year}-${month}-${day} ${hours}:${minutes}`;
  };

  return {
    'dateTimeStart': formatDateTime(start),
    'dateTimeEnd': formatDateTime(end),
  };

}