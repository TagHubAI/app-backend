export function isTouchEvent(e) {
    return window.TouchEvent && e instanceof window.TouchEvent;
}
export function calculateSize(element, innerOnly) {
    let width = element.clientWidth;
    let height = element.clientHeight;
    if (innerOnly) {
        const style = getComputedStyle(element);
        width =
            width -
                parseFloat(style.getPropertyValue('padding-left')) -
                parseFloat(style.getPropertyValue('padding-right'));
        height =
            height -
                parseFloat(style.getPropertyValue('padding-top')) -
                parseFloat(style.getPropertyValue('padding-bottom'));
        return { width, height };
    }
    return { width, height };
}
export function clampValue(value, min, max) {
    return value < min ? min : value > max ? max : value;
}
export function resolveSpeed(value) {
    if (value === undefined)
        return 0;
    if (typeof value === 'number')
        return value;
    const timeRE = /^((\d+)?\.?\d+?)(ms|s)?$/;
    const match = value.match(timeRE);
    if (match) {
        const [, number, , unit = 'ms'] = match;
        return Number(number) * (unit === 'ms' ? 1 : 1000);
    }
    return 0;
}
export function getDisplayIndex(current, length, duplicatedable) {
    return !duplicatedable
        ? current
        : current === 0
            ? length - 3
            : current === length - 1
                ? 0
                : current - 1;
}
export function getRealIndex(current, duplicatedable) {
    return !duplicatedable ? current : current + 1;
}
export function getPrevIndex(current, length, duplicatedable) {
    if (current < 0)
        return null;
    return current === 0 ? (duplicatedable ? length - 1 : null) : current - 1;
}
export function getNextIndex(current, length, duplicatedable) {
    if (current > length - 1)
        return null;
    return current === length - 1 ? (duplicatedable ? 0 : null) : current + 1;
}
