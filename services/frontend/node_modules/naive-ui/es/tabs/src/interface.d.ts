import { Ref, CSSProperties } from 'vue';
export declare type TabsType = 'line' | 'card' | 'bar' | 'segment';
export declare type OnUpdateValue = (value: string & number) => void;
export declare type OnUpdateValueImpl = (value: string | number) => void;
export declare type OnClose = (name: string & number) => void;
export declare type OnCloseImpl = (name: string | number) => void;
export declare type OnBeforeLeave = (name: string & number, oldName: string & number & null) => boolean | Promise<boolean>;
export declare type OnBeforeLeaveImpl = (name: string | number, oldName: string | number | null) => boolean | Promise<boolean>;
export interface TabsInjection {
    mergedClsPrefixRef: Ref<string>;
    valueRef: Ref<string | number | null>;
    typeRef: Ref<TabsType>;
    closableRef: Ref<boolean>;
    tabStyleRef: Ref<string | CSSProperties | undefined>;
    paneClassRef: Ref<string | undefined>;
    paneStyleRef: Ref<string | CSSProperties | undefined>;
    tabChangeIdRef: {
        id: number;
    };
    onBeforeLeaveRef: Ref<OnBeforeLeave | undefined>;
    triggerRef: Ref<'click' | 'hover'>;
    activateTab: (panelName: string | number) => void;
    handleClose: (panelName: string | number) => void;
    handleAdd: () => void;
}
export declare type Addable = boolean | {
    disabled?: boolean;
};
export declare const tabsInjectionKey: import("vue").InjectionKey<TabsInjection>;
export interface TabsInst {
    syncBarPosition: () => void;
}
