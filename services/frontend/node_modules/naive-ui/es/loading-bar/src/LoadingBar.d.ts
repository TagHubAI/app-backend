declare const _default: import("vue").DefineComponent<{}, {
    mergedClsPrefix: import("vue").Ref<string>;
    loadingBarRef: import("vue").Ref<HTMLElement | null>;
    started: import("vue").Ref<boolean>;
    loading: import("vue").Ref<boolean>;
    entering: import("vue").Ref<boolean>;
    transitionDisabled: import("vue").Ref<boolean>;
    start: (fromProgress?: number, toProgress?: number, status?: 'starting' | 'error') => Promise<void>;
    error: () => void;
    finish: () => void;
    handleEnter: () => void;
    handleAfterEnter: () => void;
    handleAfterLeave: () => Promise<void>;
    mergedLoadingBarStyle: import("vue").ComputedRef<string | import("vue").CSSProperties | undefined>;
    cssVars: import("vue").ComputedRef<{
        '--n-height': string;
        '--n-color-loading': string;
        '--n-color-error': string;
    }> | undefined;
    themeClass: import("vue").Ref<string> | undefined;
    onRender: (() => void) | undefined;
}, {}, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, import("vue").EmitsOptions, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{}>>, {}>;
export default _default;
