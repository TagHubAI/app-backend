export declare type DataTableSelectionOption = 'all' | 'none';
declare const _default: import("vue").DefineComponent<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
}, {
    handleSelect: import("vue").ComputedRef<(key: string | number) => void>;
    options: import("vue").ComputedRef<{
        label: string;
        key: string | number;
    }[]>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
}>>, {}>;
export default _default;
