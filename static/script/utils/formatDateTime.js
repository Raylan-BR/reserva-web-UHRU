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