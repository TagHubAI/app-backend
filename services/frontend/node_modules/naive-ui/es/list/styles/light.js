import { composite } from 'seemly';
import { commonLight } from '../../_styles/common';
export const self = (vars) => {
    const { textColor2, cardColor, modalColor, popoverColor, dividerColor, borderRadius, fontSize } = vars;
    return {
        textColor: textColor2,
        color: cardColor,
        colorModal: modalColor,
        colorPopover: popoverColor,
        borderColor: dividerColor,
        borderColorModal: composite(modalColor, dividerColor),
        borderColorPopover: composite(popoverColor, dividerColor),
        borderRadius,
        fontSize
    };
};
const listLight = {
    name: 'List',
    common: commonLight,
    self
};
export default listLight;
