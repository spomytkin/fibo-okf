---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: step up bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond with a coupon that increases (steps up) while the bond is outstanding
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The step change may be one time, or occur according to a schedule or at regular intervals.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: step down bond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SteppedCouponTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasInterestPaymentTerms
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/StepUpBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: step up bond
type: Ontology Class
---

# step up bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/StepUpBond>

## Definition

bond with a coupon that increases (steps up) while the bond is outstanding

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Subclass of**: [FixedIncomeSecurity](/concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)

## Constraints

- **[hasInterestPaymentTerms](/concepts/fibo/SEC/Debt/DebtInstruments/hasInterestPaymentTerms.md)**: some values from of type [SteppedCouponTerms](/concepts/fibo/SEC/Debt/Bonds/SteppedCouponTerms.md)

## Annotations

- **label**: step up bond
- **definition**: bond with a coupon that increases (steps up) while the bond is outstanding
- **explanatoryNote**: The step change may be one time, or occur according to a schedule or at regular intervals.
- **synonym**: step down bond

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
