---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pass through m b s deal prospectus
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The written prospectus for an agency, pass through issue of Mortgage Backed Securities
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurityOfferingProspectus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurityOfferingProspectus
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSDealProspectus
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: pass through m b s deal prospectus
type: Ontology Class
---

# pass through m b s deal prospectus

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSDealProspectus>

## Definition

The written prospectus for an agency, pass through issue of Mortgage Backed Securities

## Relationships

- **Subclass of**: [MortgageBackedSecurityOfferingProspectus](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurityOfferingProspectus.md)

## Constraints

- **Disjoint with**: [TranchedMBSDealProspectus](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus.md)

## Annotations

- **label** (en): pass through m b s deal prospectus
- **definition** (en): The written prospectus for an agency, pass through issue of Mortgage Backed Securities

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
