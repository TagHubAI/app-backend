import { Ref, ComponentPublicInstance } from 'vue';
export declare function isTouchEvent(e: MouseEvent | TouchEvent): e is TouchEvent;
declare type RefType = HTMLElement | ComponentPublicInstance;
declare type RefKey = number;
declare type RefsValue<T extends RefType> = Map<RefKey, T>;
export declare function useRefs<T extends RefType>(): [
    Ref<RefsValue<T>>,
    (key: RefKey) => (el: any) => void
];
export {};
