---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond insurance
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: insurance policy that a bond issuer purchases that guarantees the repayment of the principal and all associated
      interest payments to the bondholders in the event of default
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/InsurancePolicy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/InsurancePolicy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondInsurance
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: bond insurance
type: Ontology Class
---

# bond insurance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondInsurance>

## Definition

insurance policy that a bond issuer purchases that guarantees the repayment of the principal and all associated interest payments to the bondholders in the event of default

## Relationships

- **Subclass of**: [InsurancePolicy](/concepts/fibo/FBC/DebtAndEquities/Guaranty/InsurancePolicy.md)

## Annotations

- **label**: bond insurance
- **definition**: insurance policy that a bond issuer purchases that guarantees the repayment of the principal and all associated interest payments to the bondholders in the event of default

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
