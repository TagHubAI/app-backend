export interface Size {
    width: number;
    height: number;
}
export declare function isTouchEvent(e: MouseEvent | TouchEvent): e is TouchEvent;
export declare function calculateSize(element: HTMLElement, innerOnly?: boolean): Size;
export declare function clampValue(value: number, min: number, max: number): number;
export declare function resolveSpeed(value?: string | number): number;
export declare function getDisplayIndex(current: number, length: number, duplicatedable?: boolean): number;
export declare function getRealIndex(current: number, duplicatedable?: boolean): number;
export declare function getPrevIndex(current: number, length: number, duplicatedable?: boolean): number | null;
export declare function getNextIndex(current: number, length: number, duplicatedable?: boolean): number | null;
