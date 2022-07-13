import type { ThemeCommonVars } from '../../_styles/common';
import { Theme } from '../../_mixins';
export declare const self: (vars: ThemeCommonVars) => {
    textColor: string;
    color: string;
    colorModal: string;
    colorPopover: string;
    borderColor: string;
    borderColorModal: string;
    borderColorPopover: string;
    borderRadius: string;
    fontSize: string;
};
export declare type ListThemeVars = ReturnType<typeof self>;
declare const listLight: Theme<'List', ListThemeVars>;
export default listLight;
export declare type ListTheme = typeof listLight;
