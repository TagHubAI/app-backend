declare const _default: import("vue").DefineComponent<{}, {
    mergedClsPrefix: import("vue").ComputedRef<string>;
    selfElRef: import("vue").Ref<HTMLElement | undefined>;
    isPrev: import("vue").ComputedRef<boolean>;
    isNext: import("vue").ComputedRef<boolean>;
    isActive: import("vue").ComputedRef<boolean>;
    index: import("vue").ComputedRef<number | undefined>;
    style: import("vue").ComputedRef<any>;
    prevSlideStyle: import("vue").Ref<string | import("vue").CSSProperties | undefined>;
    nextSlideStyle: import("vue").Ref<string | import("vue").CSSProperties | undefined>;
    handleClick: (event: MouseEvent) => void;
}, {}, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, import("vue").EmitsOptions, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{}>>, {}>;
export default _default;
