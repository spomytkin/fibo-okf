---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - PDIED
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: premiumDiscountAtIED
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: "Total original premium or discount that has been set at CDD and will be added to the (notional) cash flow at IED\
      \ (cash flow at IED = NT+PDIED, w.r.t. an RPA CT). \n\nNegative value for discount and positive for premium.\n\nNote,\
      \ similar to interest the PDIED portion is part of P&L."
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: PDIED
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Premium Discount At IED
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PDIED
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - PDIED
type: Ontology Individual
---

# ACTUS contract term - PDIED

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-PDIED>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - PDIED
- **hasParameterName**: premiumDiscountAtIED
- **hasDescription**: Total original premium or discount that has been set at CDD and will be added to the (notional) cash flow at IED (cash flow at IED = NT+PDIED, w.r.t. an RPA CT).   Negative value for discount and positive for premium.  Note, similar to interest the PDIED portion is part of P&L.
- **hasTag**: PDIED
- **hasTextualName**: Premium Discount At IED

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
