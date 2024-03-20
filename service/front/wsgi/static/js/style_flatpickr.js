flatpickr.localize(flatpickr.l10ns.ja);
flatpickr('#possibleDate', {
    altInput: true,
    altFormat: "Y-m-d",
    dateFormat: "Y-m-d",
    mode: "multiple",
    conjunction: "\r\n",
    inline: true,
    static: true,
    onChange(selectedDates, dateStr, instance) {
        $('#inport').html(instance.altInput.value);
    },
});
