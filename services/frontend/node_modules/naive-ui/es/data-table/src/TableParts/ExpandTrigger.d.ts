import { PropType } from 'vue';
declare const _default: import("vue").DefineComponent<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    expanded: BooleanConstructor;
    loading: BooleanConstructor;
    onClick: {
        type: PropType<() => void>;
        required: true;
    };
}, unknown, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, Record<string, any>, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    expanded: BooleanConstructor;
    loading: BooleanConstructor;
    onClick: {
        type: PropType<() => void>;
        required: true;
    };
}>>, {
    expanded: boolean;
    loading: boolean;
}>;
export default _default;
