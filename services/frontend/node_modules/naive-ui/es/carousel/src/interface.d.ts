import { CSSProperties, Ref } from 'vue';
export declare const tuple: <T extends string[]>(...args: T) => T;
export declare type ElementOf<T> = T extends Array<infer E> ? E : T extends ReadonlyArray<infer F> ? F : never;
export interface CarouselMethodsInjection {
    to: (index: number) => void;
    prev: () => void;
    next: () => void;
    isVertical: () => boolean;
    isHorizontal: () => boolean;
    isPrev: (slide: number | HTMLElement) => boolean;
    isNext: (slide: number | HTMLElement) => boolean;
    isActive: (slide: number | HTMLElement) => boolean;
    isPrevDisabled: () => boolean;
    isNextDisabled: () => boolean;
    getCurrentIndex: () => number;
    getSlideIndex: (slide: number | HTMLElement) => number;
    getSlideStyle: (slide: HTMLElement) => any;
    addSlide: (slide?: HTMLElement) => void;
    removeSlide: (slide?: HTMLElement) => void;
    onCarouselItemClick: (index: number, event: MouseEvent) => void;
    prevSlideStyleRef: Ref<CSSProperties | string | undefined>;
    nextSlideStyleRef: Ref<CSSProperties | string | undefined>;
}
export declare const carouselMethodsInjectionKey: import("vue").InjectionKey<CarouselMethodsInjection>;
export interface CarouselInst {
    getCurrentIndex: () => number;
    to: (index: number) => void;
    prev: () => void;
    next: () => void;
}
export declare const enum DragFlags {
    NORMAL = 1,
    START = 2,
    PROGRESS = 4,
    SUCCESS = 8,
    FAIL = 16,
    END = 32
}
