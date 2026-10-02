---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-guarantor debt basket
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of debt instruments that include a provision allowing certain subsidiaries within a corporate group, which
      are not part of the loan guarantee, to incur a specified amount of indebtedness
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A non-guarantor debt basket is often also permitted to be secured by assets of a subsidiary other than the issuer/borrower
      or guarantors.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In U.S. law, a non-guarantor debt basket is a shared basket in an amount not to exceed the greater of $150,000,000
      and 20% of Consolidated EBITDA for the most recently ended Test Period at any time outstanding that may be used for
      (A) the incurrence of certain Indebtedness by Restricted Subsidiaries that are not Loan Parties under Sections 6.01(a)(xii),
      6.01(a)(xix) and 6.01(a)(xx) and (B) Secured Cash Management Obligations of any Restricted Subsidiary that is not a
      Loan Party.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/Non-GuarantorDebtBasket
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: non-guarantor debt basket
type: Ontology Class
---

# non-guarantor debt basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/Non-GuarantorDebtBasket>

## Definition

basket of debt instruments that include a provision allowing certain subsidiaries within a corporate group, which are not part of the loan guarantee, to incur a specified amount of indebtedness

## Relationships

- **Subclass of**: [BasketOfDebtInstruments](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md)

## Annotations

- **label** (en): non-guarantor debt basket
- **definition** (en): basket of debt instruments that include a provision allowing certain subsidiaries within a corporate group, which are not part of the loan guarantee, to incur a specified amount of indebtedness
- **explanatoryNote** (en): A non-guarantor debt basket is often also permitted to be secured by assets of a subsidiary other than the issuer/borrower or guarantors.
- **explanatoryNote** (en): In U.S. law, a non-guarantor debt basket is a shared basket in an amount not to exceed the greater of $150,000,000 and 20% of Consolidated EBITDA for the most recently ended Test Period at any time outstanding that may be used for (A) the incurrence of certain Indebtedness by Restricted Subsidiaries that are not Loan Parties under Sections 6.01(a)(xii), 6.01(a)(xix) and 6.01(a)(xx) and (B) Secured Cash Management Obligations of any Restricted Subsidiary that is not a Loan Party.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
