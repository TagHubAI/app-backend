import { Ref, CSSProperties, VNode } from 'vue';
export declare type PopoverTrigger = 'click' | 'hover' | 'focus' | 'manual';
export interface PopoverInst {
    syncPosition: () => void;
    setShow: (value: boolean) => void;
}
export declare type PopoverBodyInjection = Ref<HTMLElement | null> | null;
export declare const popoverBodyInjectionKey: import("vue").InjectionKey<PopoverBodyInjection>;
export declare type InternalRenderBody = (className: any, ref: Ref<HTMLElement | null>, style: Ref<CSSProperties>, onMouseenter: (e: MouseEvent) => void, onMouseleave: (e: MouseEvent) => void) => VNode;
