---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: treasury inflation-protected security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: variable income bond whose principal is indexed to inflation or deflation and thus changes over the life of the
      security
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: TIPS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Treasury Inflation-Protected Securities, or TIPS, provide protection against inflation. The principal of a TIPS
      increases with inflation and decreases with deflation, as measured by the Consumer Price Index. When a TIPS matures,
      you are paid the adjusted principal or original principal, whichever is greater.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.treasurydirect.gov/indiv/products/prod_tips_glance.htm
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/InflationLinkedBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/InflationLinkedBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/USTreasurySecurity
  - concept: /concepts/fibo/SEC/Debt/Bonds/VariablePrincipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariablePrincipalBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryInflationProtectedSecurity
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: treasury inflation-protected security
type: Ontology Class
---

# treasury inflation-protected security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryInflationProtectedSecurity>

## Definition

variable income bond whose principal is indexed to inflation or deflation and thus changes over the life of the security

## Relationships

- **See also**: [prod_tips_glance.htm](<https://www.treasurydirect.gov/indiv/products/prod_tips_glance.htm>)
- **Subclass of**: [InflationLinkedBond](/concepts/fibo/SEC/Debt/Bonds/InflationLinkedBond.md)
- **Subclass of**: [USTreasurySecurity](/concepts/fibo/SEC/Debt/Bonds/USTreasurySecurity.md)
- **Subclass of**: [VariablePrincipalBond](/concepts/fibo/SEC/Debt/Bonds/VariablePrincipalBond.md)

## Annotations

- **label**: treasury inflation-protected security
- **definition**: variable income bond whose principal is indexed to inflation or deflation and thus changes over the life of the security
- **abbreviation**: TIPS
- **explanatoryNote**: Treasury Inflation-Protected Securities, or TIPS, provide protection against inflation. The principal of a TIPS increases with inflation and decreases with deflation, as measured by the Consumer Price Index. When a TIPS matures, you are paid the adjusted principal or original principal, whichever is greater.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
