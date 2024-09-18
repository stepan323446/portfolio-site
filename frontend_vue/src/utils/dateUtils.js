export function formatDate(dateStr) {
    let date = new Date(dateStr);
    const options = { day: 'numeric', month: 'long', year: 'numeric' };

    const formattedDate = date.toLocaleDateString('en-US', options);
    return formattedDate;
}